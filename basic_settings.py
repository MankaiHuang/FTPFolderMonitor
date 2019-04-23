import os

uploading_checking_break_minutes = 0.1
uploading_checking_time_out_hours = 2
main_program_break_minutes = 0.1
ending_hour = 9

# The folder will be monitored
ftp_folder = r'C:\ftp_test\source'

# The folder where the source files will be moved into.
target_root_folder = r'c:\ftp_test\target'

# The folder where the source files will be archived into.
archive_root_folder = r'c:\ftp_test\archive'

# The folder is used to save all logs files.
main_log_folder = r'c:\ftp_test\logs'

for item in [ftp_folder, target_root_folder, archive_root_folder, main_log_folder]:
    if not os.path.isdir(item):
        raise Exception('{} does not exist'.format(item))
