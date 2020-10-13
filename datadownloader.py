import requests, os, zipfile, stat, re

data_directory = 'data'

# Downloads files from Google Drive. 
def download_google(id, destination):
    URL = 'https://docs.google.com/uc?export=download'

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    
    
# Gets token
def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

# Writes chunks
def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                
# Downloads files from url
def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
            
# Downloads files from url
def download_url(url, save_path):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content():
            fd.write(chunk)
            
# 'DatasetName' : 'File ID'
classical_SR_datasets = {
    'BSDS100': '1EWEsfsgElkNvOcJwZLDe2TeDIMhr6SpH',
    'BSDS200': '1hIYAIODXT6GksNuk0EHiwgnVxZlDHUAI',
    'General100': '1Y4R8STXyPcOOykutbAJpMsH5O5n2NdFF',
    'historical': '17Rq-4gm1_rJX3KB2jolcqMGWiSSmQIWz',
    'manga109': '15cAVM4BJtSGpduLufqDqfQV75m-Pfepi',
    'Set5': '1RtyIeUFTyW8u7oa4z7a0lSzT3T1FwZE9',
    'Set14': '1vsw07sV8wGrRQ8UARe2fO5jjgy9QJy_E',
    'T91': '1dfsToAYgecVARKjw2wtQS5tsn6pzG6pr',
    'urban100': '1XaY-tnBP_z21WKgOCeXBa9r-KJyBMbgZ'
}

# Make data directory
if not os.path.isdir(data_directory):
    os.mkdir(data_directory)

# Download and unzip all classical SR datasets
for dataset in classical_SR_datasets:
    dataset_directory = data_directory + '/' + dataset
    if os.path.isdir(dataset_directory):
        print(dataset_directory + ' already exists.')
    else:
        # Download .zip files from Google Drive
        file_id = datasets[dataset]
        zip_path = data_directory + '/' + dataset + '.zip'
        if not os.path.isfile(dataset + '.zip'):
            print("Downloading " + dataset + '.zip')
            download_google(file_id, zip_path)
        # Unzip .zip files
        print("Unzipping " + dataset + '.zip')
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(data_directory)
        # Delete .zip file
        print("Deleting " + dataset + '.zip')
        os.remove(zip_path)
    print()
    
