# Provenance

Paper: Rayaprolu, H. S., Wu, H., Lahoorpoor, B., and Levinson, D. (2022). Maximizing access in transit network design. Journal of Public Transportation, 24, 100027. https://doi.org/10.1016/j.jpubtr.2022.100027

This package was curated from the Liverpool/iMove project materials staged in this workbench and from the existing 2022-04 Liverpool access package. The published paper states that 195 GTFS scenarios were created from route geometries, stop locations, and service frequencies; that QGIS was used for street network and route/stop geometry setup; that a Python program generated GTFS files; and that OpenTripPlanner was used for isochrone queries.

The included archive boundary is the hydrated local evidence that can be interpreted now: the GTFS-generation notebooks and Python helper, route/stop/travel-time CSVs, current GTFS source zip, scenario GIS layers, compressed large shapefile bundles, and access/frequency matrix tables and notebooks. OpenTripPlanner and QGIS are external runtimes, not bundled dependencies.

The exact custom OTP batch-query wrapper is not treated as an outstanding artifact. The live Dropbox folder contains generated scenario zip names under the GTFS output tree that are cloud-only zero-byte entries in the current local copy; because the package includes the generation workflow, inputs, GIS layers, and access outputs, that does not block public upload review.

Curated: 2026-05-19 19:59:11
