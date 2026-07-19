from faker import Faker
import pandas as pd
import random
import os

from config import *

fake = Faker()

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("Generating master data...")
