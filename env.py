import os

""" This is purely for the dev environment, this wont be pushed live """

os.environ.setdefault("SECRET_KEY", 
    "z64wjo%vxy9osmn!kl+3dxo5%9eo_+)6k+4ve(@%g4zcp=w(74")
    
os.environ.setdefault("DATABASE_URL", 
    "postgres://ncavbwoodhiovk:79276cd215ea82bbc3852d1fc70295ce06335ea7a508dd077fbb1b88e7bab8d6@ec2-54-228-181-43.eu-west-1.compute.amazonaws.com:5432/db92pfeaidkbu0")