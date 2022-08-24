<h2 align="center">Fullstory API Python Client for Marketers and Data Engineers</h2>

# I. Introduction
## 📦 About FullStory
[FullStory](https://fullstory.com/) captures and replays your users' experiences so that you can build a better website or native mobile application. You can shape FullStory to your specific needs using our simple Client API and secure HTTP API.

## 😎 About this package
This Python Client allow you control user data and export all event data captured by FullStory for external analysis with ease. All of the functions in this package are using the HTTPS API end point from FullStory [here](https://developer.fullstory.com/introduction).

## ⚔️ Who should use this package?
- 💌 Marketers: Using a Standard API key, you can interact with FullStory in multiple ways. You can do basic data export operations such as: Exporting users' recorded events, user's visited pages, etc.
- 📝 Data Engineers / Data Analyst: Using an Admin API key, you can retrieve all kinds of data available on FullStory. You can also use this package to build your data pipeline to store FullStory in your data warehouse.

# II. References
## 2.1. How to install this package?
- Using pip to installed pre-builded package on Pypip `pip install fullstory_api`
- If you want to use the latest fullstory_api version instead of the stable one, you can install it from source with the following command:
`pip install git+https://github.com/thinh-vu/fullstory_api.git@main`

## 2.2. Available functions

There are 7 functions available in this package to interact with FullStory as follow:

### USERS

- `fs_user_export`: Export events or pages of historical data of a specific user by the userId. Reference [here](https://developer.fullstory.com/get-data-export)
 
- `fs_GetUser`: Get a summary of user information in a DataFrame format. Reference [here](https://developer.fullstory.com/get-user)

### SEGMENTS

- `fs_list_segment`: Get a list of all available segments on your Fullstory account. Reference [here](https://developer.fullstory.com/list-segments)

- `fs_segment_export`: Return the segment export as a DataFrame. This function combine the operation of 3 other functions at 1 including fs_schedule_segment_export, fs_operation_status, fs_export_result.

- `fs_schedule_segment_export`: Schedules an export based on the provided segment and returns the operationId. Reference [here](https://developer.fullstory.com/create-segment-export)
The progress and results of the export can be fetched from the operations API

### GET OPERATION

- `fs_operation_status`: Get details about a specific operation. Return a "searchExportId" that can be used to retrieve the export result. Reference [here](https://developer.fullstory.com/get-operation)

### SEARCH

- `fs_export_result`: Gets the results for a scheduled export. Return a link which can be use to retrieve the exported CSV gzip file. Reference [here](https://developer.fullstory.com/get-export-results)

# III. Quick tips
- Use the command dir(fullstory_api) To list down all of the available functions of this module in the Python IDE.
- Using pre-built function `fs_help(function_name)` to print the docstring helper of that function. For instance, you can type the command to the terminal with `fs_help(fs_export_result).`
- Using the command `from fullstory_api import *` to import all functions in this module to the Python Interpreter.

# IV. 🙋‍♂️ Contact Information
You can contact me at one of my social network profiles:

- 💼 LinkedIn: https://linkedin.com/in/thinh-vu
- :octocat: GitHub: https://github.com/thinh-vu
