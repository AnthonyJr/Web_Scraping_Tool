from lxml import html 
import requests 
from itertools import izip 

def main(): 

	r = open('counties_ky.txt', 'r+'); 
	r2 = open('cities_ky.txt', 'r+')
	w = open('counties')

	
