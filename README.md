<h2 align="center">Fullstory API Python Client for Marketers and Data Engineers</h2>

<div id="badges" align="center">
<img src="https://img.shields.io/pypi/pyversions/pydata_master?logoColor=brown&style=plastic" alt= "Version"/>
<img src="https://img.shields.io/pypi/dm/pydata_master" alt="Download Badge"/>
<img src="https://img.shields.io/github/last-commit/thinh-vu/pydata_master" alt="Commit Badge"/>
<img src="https://img.shields.io/github/license/thinh-vu/pydata_master?color=red" alt="License Badge"/>
</div>

# I. Introduction
## 📦 About FullStory
[FullStory](https://fullstory.com/) captures and replays your users' experiences so that you can build a better website or native mobile application. You can shape FullStory to your specific needs using our simple Client API and secure HTTP API.

## 😎 About this package
This Python Client allows you to control user data and export all event data captured by FullStory for external analysis with ease. All of the functions in this package use the HTTPS API endpoint from FullStory [here](https://developer.fullstory.com/introduction).

## ⚔️ Who should use this package?
- 💌 Marketers: Using a Standard API key, you can interact with FullStory in multiple ways. You can do basic data export operations such as: Exporting users' recorded events; user's visited pages, etc.
- 📝 Data Engineers / Data Analyst: Using an Admin API key, you can retrieve all kinds of data available on FullStory. You can also use this package to build your data pipeline to store FullStory in your data warehouse.

# II. References
## 2.1. How to install this package?
- Using pip to install the pre-built package on Pypip `pip install fullstory_api`
- If you want to use the latest fullstory_api version instead of the stable one, you can install it from the source with the following command:
`pip install git+https://github.com/thinh-vu/fullstory_api.git@main`

## 2.2. Available functions

There are 7 functions available in this package to interact with FullStory as follows:

### USERS

- `fs_user_export`: Export events or pages of historical data of a specific user by the userId. Reference [here](https://developer.fullstory.com/get-data-export)
 
- `fs_GetUser`: Get a summary of user information in a DataFrame format. Reference [here](https://developer.fullstory.com/get-user)

### SEGMENTS

- `fs_list_segment`: Get a list of all available segments on your Fullstory account. Reference [here](https://developer.fullstory.com/list-segments)

- `fs_segment_export`: Return the segment export as a DataFrame. This function combines the operation of 3 other functions at 1, including fs_schedule_segment_export, fs_operation_status, fs_export_result.

- `fs_schedule_segment_export`: Schedules an export based on the provided segment and returns the operationId. Reference [here](https://developer.fullstory.com/create-segment-export)
The progress and results of the export can be fetched from the operations API

### GET OPERATION

- `fs_operation_status`: Get details about a specific operation. Return a "searchExportId" that can be used to retrieve the export result. Reference [here](https://developer.fullstory.com/get-operation)

### SEARCH

- `fs_export_result`: Gets the results for a scheduled export. Return a link that can be used to retrieve the exported CSV gzip file. Reference [here](https://developer.fullstory.com/get-export-results)

# III. Quick tips
- Use the command dir(fullstory_api) To list down all of the available functions of this module in the Python IDE.
- Using pre-built function `fs_help(function_name)` to print the docstring helper of that function. For instance, you can type the command to the terminal with `fs_help(fs_export_result).`
- Use the command `from fullstory_api import *` to import all functions in this module to the Python Interpreter.

# IV. 🙋‍♂️ Contact Information
<div id="badges" align="center">
  <a href="https://www.linkedin.com/in/thinh-vu">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.messenger.com/t/mr.thinh.ueh">
    <img src="https://img.shields.io/badge/Messenger-00B2FF?style=for-the-badge&logo=messenger&logoColor=white" alt="Messenger Badge"/>
  <a href="https://www.youtube.com/channel/UCYgG-bmk92OhYsP20TS0MbQ">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  </a>
    <a href="https://github.com/thinh-vu">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Github Badge"/>
  </a>
</div>

---

If you want to support my open-source projects, you can "buy me a coffee" via [Patreon](https://patreon.com/thinhvu?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=creatorshare_creator) or Momo e-wallet (VN). Your support will help to maintain my blog hosting fee & to develop high-quality content.

![momo-qr](https://github.com/thinh-vu/vnstock/blob/main/src/momo-qr-thinhvu.jpeg?raw=true)

