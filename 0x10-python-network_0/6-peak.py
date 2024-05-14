#!/usr/bin/python3
"""Function that finds a peak in an array of unsorted integers"""

def find_peak(list_of_integers):
	"""finds a peak"""
	if not list_of_integers:
		return None
	
	def find_peak_(arr, low, high, n):
		mid = low + (high - low) // 2

		# check if mid element is peak
		if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid]):
			return arr[mid]
		
		#if left neighbor is greater, find peak n the left half
		if mid > 0 and arr[mid - 1] > arr[mid]:
			return find_peak_(arr, low, mid - 1, n)
		
		# If the right neighbor is greater, find peak in the right half
		return find_peak_(arr, mid + 1, high, n)
	return find_peak_(list_of_integers, 0, len(list_of_integers) - 1, len(list_of_integers))
