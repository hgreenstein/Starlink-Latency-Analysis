# Starlink-Latency-Analysis
Analysis of real-world performance of Starlink's Satellite Networks collaboration with: Maheer Aeron, Matthew Cafiero, Joshua Church and Skyler Krouse

## Project Goal: 
Our goal for this project was to analyze the latency of Starlink to assess how and why the
latency of different Starlink terminals changes over time and location. To do so, we gathered a
collection of RIPE Atlas probes connected to Starlink terminals and pinged them to the same
site at the same time over the course of a day to compare how each terminal’s latency changes

## Notable Conclusions:
- Starlink does not provide users its promised latency of 25 ms. Looking at the average
hourly latency of each probe no probe ever achieved a sustained latency at
this promise. Most probes never reached such an average latency at any point during our data
collection
- Starlink is not transparent with the true consistency of their product.
Our results prove that there is variation in latency by location and time. While this would be
expected with any internet product, Starlinks advertising never speaks to such variation for
users, and if anything, often implies the opposite

## Full Report:
[Avalible Here](https://harrisgreenstein.com/assets/starlinkReport-65588e38.pdf)

## Important files:

### [starlinkProbes.py](/starlinkProbes.py)

This simply retrieves all avalible RIPE Atlas probes that match Starlink's IPv4

### [measurements.py](/measurements.py)

This covers the requesting and fetching of the main measurements we used to measure Starlink's latency and traceroutes
- The first measurements were a series of ping requests that occured every 15 minutes for a 24 hour period around the globe
- The second measurements were a series of traceroutes from the same probes to the same target to understand what ground stations and satellites are being used and where unexpected latency is originating from
- The main target of our traceroute was bing.com as it has globally distributed servers that could try to minimize the latency from starlink ground station to target
- Traceroutes and measurements were correlated with estimated satellite positions at the given measurement times to attempt to explain our conclusions and claims regarding the measurements, full details and raw data avalible in the full report
