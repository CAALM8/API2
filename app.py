import streamlit as st
import requests

st.set_page_config(page_title="Met Museum Collections API", page_icon="🎨", layout="wide")

st.title("🎨 Met Museum Collections Search API")
st.write(
    "Search artworks from the Metropolitan Museum of Art. "
    "Enter any keyword (e.g., 'dog', 'impressionism', 'ancient') to find related artworks."
)

search_query = st.text_input("🔍 Search collections", placeholder="Enter keyword...").strip()

if search_query:
    st.info("Searching The Met Museum collection...")
    # Step 1: Search API
    search_url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={search_query}"
    search_resp = requests.get(search_url).json()
    objectIDs = search_resp.get("objectIDs", [])
    total = search_resp.get("total", 0)
    
    if total > 0 and objectIDs:
        st.write(f"### Found {total} object(s)")
        # Limit results to 20 items to avoid too many requests
        for obj_id in objectIDs[:20]:
            obj_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
            obj_data = requests.get(obj_url).json()
            
            title = obj_data.get("title", "Unknown")
            artist = obj_data.get("artistDisplayName", "Unknown")
            date = obj_data.get("objectDate", "Unknown")
            museum_url = obj_data.get("objectURL", "#")
            image_url = obj_data.get("primaryImageSmall", "")
            
            with st.expander(f"{title} by {artist} ({date})"):
                if image_url:
                    st.image(image_url, use_column_width=True)
                st.markdown(f"**Artist:** {artist}")
                st.markdown(f"**Date:** {date}")
                st.markdown(f"[🌐 Museum Link]({museum_url})")
    else:
        st.warning("No objects found. Try another keyword.")
