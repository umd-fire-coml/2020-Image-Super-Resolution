% Script based off of: 
% https://github.com/daitao/SAN/blob/master/TestCode/Prepare_TestData_HR_LR.m  

% Downscales all single-directory datasets.
function scale_images()
clear all; close all; clc

% Datasets that will be downscaled
dataset  = {'BSDS100', 'BSDS200', 'General100', 'historical', 'manga109', 'T91', 'urban100'};
% Chose image degradation method
degradation = 'bic'; % bic, BD, DN

% File path, image file extensions, scales.
path_original = './data';
ext = {'*.jpg', '*.png', '*.bmp'};
if strcmp(degradation, 'bic') 
    scale_all = [2,3,4];
else
    scale_all = [3,4];
end

% Move images from './data/historical/LR' to './data/historical/original'
if exist('./data/historical/LR')
    movefile('./data/historical/LR/*.png', './data/historical')
    rmdir('./data/historical/LR/')
end

% Downscale all datasets
for idx_set = 1:length(dataset)
    fprintf('Processing %s:\n', dataset{idx_set});
    
    % Create './data/<dataset>/original' directory
    folder_dataset = fullfile(path_original, dataset{idx_set});
    folder_original = fullfile(folder_dataset, 'original');
    if ~exist(folder_original)
        mkdir(folder_original)
    end
    % Move all images to './data/<dataset>/original'
    movefile(fullfile(folder_dataset,'*.png'), folder_original)
    
    % Create list of all of the filepaths of the original images.
    filepaths = [];
    for idx_ext = 1:length(ext)
        filepaths = cat(1, filepaths, dir(fullfile(folder_original, ext{idx_ext})));
    end
    % Downscale the original images and write them to their scaled directories 
    for idx_im = 1:length(filepaths)
        name_im = filepaths(idx_im).name;
        fprintf('%d. %s: ', idx_im, name_im);
        im_ori = imread(fullfile(folder_original, name_im));
        if size(im_ori, 3) == 1
            im_ori = cat(3, im_ori, im_ori, im_ori);
        end
        for scale = scale_all
            fprintf('x%d ', scale);
            
            % Crop original image for scaling. 
            im_HR = modcrop(im_ori, scale);
            
            % Apply chosen degradation method to image
            if strcmp(degradation, 'bic')
                im_LR = imresize(im_HR, 1/scale, 'bicubic');
            elseif strcmp(degradation, 'BD')
                im_LR = imresize_BD(im_HR, scale, 'Gaussian', 1.6); % sigma=1.6
            elseif strcmp(degradation, 'DN')
                randn('seed',0); % For test data, fix seed. But, DON'T fix seed, when preparing training data.
                im_LR = imresize_DN(im_HR, scale, 30); % noise level sigma=30
            end
            
            % Create './data/<dataset>/LR<degradation>x<scale>/'
            folder_LR = fullfile(folder_dataset, ['LR', degradation, 'x', num2str(scale)]);
            if ~exist(folder_LR)
                mkdir(folder_LR)
            end
            % Write scaled image to directory.
            fn_LR = fullfile(folder_LR, [name_im(1:end-4), '_LR', degradation, 'x', num2str(scale), '.png']);
            imwrite(im_LR, fn_LR, 'png');
        end
        fprintf('\n');
    end
    fprintf('\n');
end
fprintf('Finished.');
end

% Crops original HR image for downscaling.
function imgs = modcrop(imgs, modulo)
if size(imgs,3)==1
    sz = size(imgs);
    sz = sz - mod(sz, modulo);
    imgs = imgs(1:sz(1), 1:sz(2));
else
    tmpsz = size(imgs);
    sz = tmpsz(1:2);
    sz = sz - mod(sz, modulo);
    imgs = imgs(1:sz(1), 1:sz(2),:);
end
end

% Applies BD degradation model to image.
function [LR] = imresize_BD(im, scale, type, sigma)
if nargin ==3 && strcmp(type,'Gaussian')
    sigma = 1.6;
end

if strcmp(type,'Gaussian') && fix(scale) == scale
    if mod(scale,2)==1
        kernelsize = ceil(sigma*3)*2+1;
        if scale==3 && sigma == 1.6
            kernelsize = 7;
        end
        kernel  = fspecial('gaussian',kernelsize,sigma);
        blur_HR = imfilter(im,kernel,'replicate');
        
        if isa(blur_HR, 'gpuArray')
            LR = blur_HR(scale-1:scale:end-1,scale-1:scale:end-1,:);
        else
            LR      = imresize(blur_HR, 1/scale, 'nearest');
        end
        % LR      = im2uint8(LR);
    elseif mod(scale,2)==0
        kernelsize = ceil(sigma*3)*2+2;
        kernel     = fspecial('gaussian',kernelsize,sigma);
        blur_HR    = imfilter(im, kernel,'replicate');
        LR= blur_HR(scale/2:scale:end-scale/2,scale/2:scale:end-scale/2,:);
        % LR         = im2uint8(LR);
    end
else
    LR = imresize(im, 1/scale, type);
end
end

% Apply DN degradation model to image.
function ImLR = imresize_DN(ImHR, scale, sigma)
% ImLR and ImHR are uint8 data
% downsample by Bicubic
ImDown = imresize(ImHR, 1/scale, 'bicubic'); % 0-255
ImDown = single(ImDown); % 0-255
ImDownNoise = ImDown + single(sigma*randn(size(ImDown))); % 0-255
ImLR = uint8(ImDownNoise); % 0-255
end
