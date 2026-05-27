.PHONY: generate serve

skimage-api.json:
	python ../myst-apidoc/npdoc2json.py skimage > skimage-api.json

# skimage2-api.json:
# 	python ../myst-apidoc/npdoc2json.py skimage2 > skimage2-api.json

generate: skimage-api.json #skimage2-api.json
	python generate-index.py

serve:
	myst start
