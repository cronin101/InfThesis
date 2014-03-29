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

.PHONY: sort_borked
sort_borked:
	python ./make_graphs.py sort_borked "Arbitrary Sort tasks" no_bespoke

.PHONY: sort_pow2
sort_pow2:
	python ./make_graphs.py sort_pow2 "Power-of-two Sort tasks" no_bespoke

all_graphs: just_map sparse_filter dense_filter mapfilter sort_borked sort_pow2
