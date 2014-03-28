.PHONY: just_map
just_map:
	python ./make_graphs.py just_map "Map tasks"

.PHONY: sparse_filter
sparse_filter:
	python ./make_graphs.py sparse_filter "Sparse Filter tasks"

.PHONY: dense_filter
dense_filter:
	python ./make_graphs.py dense_filter "Dense Filter tasks"

.PHONY: mapfilter
mapfilter:
	python ./make_graphs.py mapfilter "MapFilter tasks"

all_graphs: just_map sparse_filter dense_filter mapfilter
