import glob

from src.disk_utils import load_json, get_store_data_fname


def load_slugs_dict(num_chunks=None, keyword="pageSlug", verbose=True):
    if num_chunks is None:
        num_chunks = infer_num_chunks()

    slugs_dict = dict()

    if verbose:
        print(f"Loading store data which was saved in {num_chunks} chunks.")

    for chunk_no in range(num_chunks):
        store_data = load_json(get_store_data_fname(chunk_no))
        for e in store_data["elements"]:
            title = e["title"]
            offer_mapping = e["offerMappings"]
            namespace_mapping = e["catalogNs"]["mappings"]

            mappings = []
            if offer_mapping is not None:
                mappings += offer_mapping
            if namespace_mapping is not None:
                mappings += namespace_mapping

            for p in mappings:
                try:
                    slug = p[keyword]
                except KeyError:
                    continue

                if slug in slugs_dict:
                    slugs_dict[slug].add(title)
                else:
                    slugs_dict[slug] = {title}

    if verbose:
        print(f"#{keyword}s = {len(slugs_dict)}")

    return slugs_dict


def infer_num_chunks():
    fnames = glob.glob(get_store_data_fname("*"))
    return len(fnames)
