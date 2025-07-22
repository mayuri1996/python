
import logging

logging.basicConfig(
    level=logging.INFO,
    filename='app.log',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def runApp():
    print(f"runnng python project")
    logging.info("started project")

#it means run file only directly we cannot import this file and run 
if __name__=="__main__":
    runApp()    