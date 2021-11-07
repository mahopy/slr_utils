# slr_utils
Before starting a research project, it is necessary to know the current state of the art.
To find this out, there is the method of structured literature research (SLR).
I have done this countless times and have always encountered challenges that were easy to solve with a few lines of Python.
Like copying the titles when using Google Scholar for a forward search, for example
The resulting scripts can be found in this project and can be used by anyone under exclusion of any warranty at your own risk.

## Tools that can be found here
### Duplicate Finder (src/duplicate_finder.py)
The Duplicate Finder is useful when you need to find and mark duplicates from a large amount of paper.
For example, to avoid having to look at the same paper several times.
For this purpose, the Duplicate Finder can be given a directory in which it will then combine all CSV files in a large pool and check them for duplicates.
If it finds duplicates it marks that and in which file this title appears for the first time.

### Reference extender (src/ref_extender.py)
The Reference Extender can be seen as the "precursor" of the Duplicate Finder.
It does nothing else than adding the title of the contained file to the front of a list of titles.
For example, if the file is called "acm_foreward_search", this is added to the front of all the titles it contains.
So the Duplicate Finder knows later in which file this title has appeared for the first time.

### Google Scholar Meta Retriever (src/google_scholar_meta_retriever.py)
The Google Scholar Meta Retriever is designed to automatically evaluate the search results for a topic from Google Scholar.
For this, however, the search results must be downloaded via the "Save as" dialog in the browser.
If you save all pages of a search (page 1, page 2, page 3) in a folder and apply the meta retriever to it, it will automatically find and copy all titles into one file.