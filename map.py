import folium

locations = {
    '1005627': ('Port-au-Prince, Haiti', 18.5944, -72.3074),
    '24742': ('Three Bridges, Australia', -37.9167, 145.2333),
    '26696': ('Monsures, France', 49.7425, 1.9636),
    '1005561': ('London, UK (1)', 51.5074, -0.1278),
    '61366': ('London, UK (2)', 51.5100, -0.1300),
    '35751': ('Newport, Isle of Wight, UK', 50.7011, -1.2929),
    '61537': ('New York, NY, USA', 40.7128, -74.0060),
    '26834': ('Limache, Chile', -33.0169, -71.2668),
    '52955': ('Tairua, New Zealand', -37.0167, 175.8500),
    '55492': ('Hay Lakes, Alberta, CA', 53.0833, -113.0833),
    '62868': ('Goldendale, WA, USA', 45.8207, -120.8217),
    '60323': ('Kitzingen, Germany', 49.7384, 10.1611),
    '1005623': ('Prague, Czech Republic', 50.0755, 14.4378),
    '17979': ('Blainslie, Scotland, UK', 55.7333, -2.8167),
    '61081': ('Beaufort, NC, USA', 34.7182, -76.6638),
    '54330': ('Wickes, MO, USA', 37.4012, -90.6412),
    '62613': ('Crook, CO, USA', 40.5942, -102.6825),
    '62365': ('Black Canyon City, AZ, USA', 34.0698, -112.1107),
    '62498': ('Lakeview, CA, USA', 33.6839, -117.1360),
    '1004978': ('Aldeno, Italy', 45.9383, 11.0700),
    '1004876': ('Gambolo, Italy', 45.2700, 8.9300),
    '20544': ('Gotelp, Poland', 53.4667, 14.7000),
    '61113': ('Butte, Alaska', 61.5456, -149.0344),
    '19983': ('Moe, Australia', -38.1761, 146.2629),
    '53798': ('Pahrump, NV, USA', 36.2083, -115.9839),
}

m = folium.Map(location=[0, 0], zoom_start=2)

for key, value in locations.items():
    folium.Marker(
        value[1:],
        popup=f"{key}: {value[0]}",
    ).add_to(m)

m.save("final_map2.html")
