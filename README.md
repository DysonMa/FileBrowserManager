# FileBrowser Manager

Provide simple CRUD of FileBrowser operations in Python, and simply profile the uploading performance with sequential and concurrent manners.

- Python: v3.9.5
- FileBrowser Docker Image: v2.23.0

## Steps

1. First, run `run.sh` to start the FileBrowser docker container
2. Config the environment variables in `.env`
3. Move your large files such as SVGs or videos to `/test_data/large_files` folder
4. Run `test_fb.py`, it will automatically create a new folder named `TEST` in FileBrowser root directory, and execute some CRUD and uploading operations to test the processing flow
5. Run `profile_performance.py` to see how much time does the FileBrowser take to upload large files

## Experimental Result

Test 440 SVG files with total 1.5GB size, and it takes 20 seconds to uploading in sequential manner, and 14 seconds to uploading in concurrent manner.