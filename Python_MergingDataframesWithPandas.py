#	1. Preparing Data
BEGIN
	#	Reading multiple data files
		filenames = ['sales1', 'sales2']
		dataframes = []		#	create list of df
		for f in filenames:
			dataframes.append(pd.read_csv(f))
			
		#	Same as above
		filenames = ['sales1', 'sales2']
		dataframes = [pd.read_csv(f) for f in filenames]
		
		#	If filenames have pattern use glob
		from glob import glob
		filenames = glob('sales*.csv')	#	All filenames that starts with sales and ends with .csv
		dataframes = [pd.read_csv(f) for f in filenames]
	
	#	Reindexing DataFrames
		#	indices - many index labels within Index data structures (meaning - some rows, but not all) indices -  result of row slicing
		#	indexes - many pandas Index data structures (meaning - refers to all indexes(all rows together)) - all column
		#	IN INDEXING AND REINDEXING ORDER IF APPLICABLE MATTERS
		
		#	To access index
		df.index
		
		#	To .reindex()
		ordered = ['Jan', 'Apr', 'Jul', 'Oct']
		df1 = df.reindex(ordered)		#	Resulting df1 will have same data as in df but rows will be in order what was in list 'ordered'
		df1.sort_index()			#	Will sort index alphabetically
		
		#	If in index what is added in reindex is value that does not correspond to any values then Nan inserted as value
			#	example: l = ['jan', 'dec']; df2 = df.reindex(l); there were no data with month 'dec' so there will be row with index dec and value Nan
			
		df3 = df.reindex(df1.index).dropna()		#	Will drop rows where all values are Nan
		
		
END


#	2. Concatenating data
BEGIN

END


#	3. Merging data
BEGIN

END


#	4. Case Study
BEGIN

END
