A Leaflet.js map created with Folium- click on the map to add markers, double-click to remove them. This map was generated with the following Python code:

```python
map_4 = folium.Map(location=[46.8527, -121.7649], tiles='Stamen Terrain',
                   zoom_start=13)
map_4.simple_marker(location=[46.8354, -121.7325], popup='Camp Muir')
map_4.click_for_marker(popup='Waypoint')
map_4.create_map(path='mtrainier.html')
```