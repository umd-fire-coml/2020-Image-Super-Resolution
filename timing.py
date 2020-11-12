{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- 0.5415525436401367 seconds --- \n"
     ]
    }
   ],
   "source": [
    "from PIL import Image\n",
    "import numpy as np\n",
    "import time\n",
    "import datagenerator\n",
    "i = 0\n",
    "start_time = time.time()\n",
    "benchmark_size = 5\n",
    "#benchmark size = # of images we want to time\n",
    "while(i < benchmark_size):\n",
    "    gen = DataGenerator('LRbicx4', 1)\n",
    "    LR, HR = gen.__getitem__(0)\n",
    "    lr = Image.fromarray(LR[0], 'RGB')\n",
    "    hr = Image.fromarray(HR[0], 'RGB')\n",
    "    i = i + 1\n",
    "    \n",
    "print(\"--- %s seconds --- \" % (time.time() - start_time))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
