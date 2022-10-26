import glob
import os

def clean_result():
    for file in glob.glob("../test_results/*"):
        os.remove(file)
        print(f"Clean {str(file)}")


clean_result()
