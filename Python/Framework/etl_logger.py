from datetime import datetime
import time

class ETLLogger:

    def __init__(self, pipeline_name):

        self.pipeline_name = pipeline_name

        self.start_time = time.time()

        self.execution_time = datetime.now()

    def success(self, records_read, records_loaded):

        end_time = time.time()

        duration = round(end_time - self.start_time, 2)

        print()

        print("=" * 65)

        print("               HELIX ETL EXECUTION REPORT")

        print("=" * 65)

        print(f"Pipeline Name      : {self.pipeline_name}")

        print(f"Execution Date     : {self.execution_time.strftime('%Y-%m-%d')}")

        print(f"Execution Time     : {self.execution_time.strftime('%H:%M:%S')}")

        print(f"Records Read       : {records_read}")

        print(f"Records Loaded     : {records_loaded}")

        print(f"Failed Records     : {records_read - records_loaded}")

        print(f"Duration (sec)     : {duration}")

        print("Status             : SUCCESS ✅")

        print("=" * 65)

    def failure(self, error):

        end_time = time.time()

        duration = round(end_time - self.start_time, 2)

        print()

        print("=" * 65)

        print("               HELIX ETL EXECUTION REPORT")

        print("=" * 65)

        print(f"Pipeline Name      : {self.pipeline_name}")

        print(f"Execution Date     : {self.execution_time.strftime('%Y-%m-%d')}")

        print(f"Execution Time     : {self.execution_time.strftime('%H:%M:%S')}")

        print(f"Duration (sec)     : {duration}")

        print("Status             : FAILED ❌")

        print()

        print("ERROR")

        print(error)

        print("=" * 65)