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
		
		df4 = df.sort_values('col1')		#	df4 - will be sorted based on values in column - 'col1'
		
		df5 = df.reindex(['jan', 'feb', 'mar', 'apr']).ffill()		
		#	Will forwardfill all NaN values with values from before. Nan values will be where no value exist for index
		
		names_1981 = pd.read_csv('names1981.csv', header=None, names=['name','gender','count'], index_col=(0,1))
			#	Result will be df with multiindexes name, gender and value count
		
		# Reindex names_1981 (19455 rows) with index of names_1881 (1935 rows): common_names
		common_names = names_1981.reindex(names_1881.index)			
			#	Result ->	1935 rows of those names from 1881 but with count values from 1981, some will have Nan (1587 final rows)
			
	#	Arithmetic with Series and DataFrames
		weather = pd.read_csv('x.csv', index_col='Date', parse_dates=True)		#	parse_dates=True will make sure that dates are understood as dates!!!!
		
		df1.divide(ser1, axis='rows')		#	.divide() gives more control than / 
		df1.pct_change() * 100		#	.pct_change() - calculates pct_change from previous date -> x(t+1)/x(t) - 1
		
		#	If 2 df added but indexes does not match, then for places where is NaN, result of sum will be Nan!
		df + df1		#	Will result with Nan where indexes does not match

		df.add(df1, fill_values=0)		#	Instead of Nan where indexes does not match (xnum + Nan = Nan) it becomes (xnum + 0 = xnum), if fill_values=0 is USED!
		df.add(df1, fill_value=0).add(df2, fill_value=0)		#	For summing up 3 df and without Nan
		
		# Rename 'F' in column names with 'C': temps_c.columns
		temps_c.columns = temps_c.columns.str.replace('F', 'C')
		
		post2008 = gdp.loc['2008':, ]		#	post2008	->	dataframe sliced on row indexes starting from 2008 year and all columns
		
		# Resample post2008 by year, keeping last(): yearly
		yearly = post2008.resample('A').last()
			#	Resampling the slice post2008 by year.  need to chain .resample() (using the alias 'A' for annual frequency) with some kind of aggregation; 
			#	you will use the aggregation method .last() to select the last element when resampling.
		
		# Compute percentage growth of yearly: yearly['growth']
		yearly['growth'] = yearly.pct_change() * 100
		
		# Convert dollars to pounds: pounds
		pounds = dollars.multiply(exchange['GBP/USD'], axis='rows')
		
		
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
