from sqlalchemy import create_engine
import sys
engine = create_engine('mysql+pymysql://root:mypassword@localhost:3306/python-sls')

sys.modules[__name__] = engine
