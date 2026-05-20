# Maximizing Access In Transit Network Design

## Bibliographic Information

- Row ID: `paper-2022-08`
- Year: 2022
- Authors: Hema S. Rayaprolu, Hao Wu, Bahman Lahoorpoor, David Levinson
- Venue: Journal of Public Transportation, 24, 100027
- DOI: [10.1016/j.jpubtr.2022.100027](https://doi.org/10.1016/j.jpubtr.2022.100027)
- Citation: Rayaprolu, H. S., Wu, H., Lahoorpoor, B., and Levinson, D. (2022). Maximizing access in transit network design. Journal of Public Transportation, 24, 100027. https://doi.org/10.1016/j.jpubtr.2022.100027

## Archive Status

- Pipeline state: `READY-TO-UPLOAD/PUBLIC`
- Audit upload action: `upload_candidate`
- Rights status: `likely_clear_with_provenance`
- Controlled access status: `none`
- Human subjects status: `no`
- Asset match status: `partial_match`
- Audit timestamp: 2026-05-19 19:59:11

## Paper Evidence

The published paper states that the study built 13 service levels for T-way routes and 13 for local routes, yielding 195 scenarios. It says GTFS files were created for each scenario from route geometries, stop locations, and frequencies; QGIS was used to set up the street network and geometries; a Python program generated GTFS files; and OpenTripPlanner was used to query travel-time isochrones for about 9000 Liverpool LGA blocks at 8:00 AM on a Wednesday.

## Included Files

- `paper/` contains the publisher-final PDF used for local audit reference.
- `code/gtfs_generation_workflow/` contains the hydrated notebooks, Python helper, route schedules, stop-by-route tables, travel-time tables, route/stop/shape inputs, and current GTFS source zip used for scenario generation.
- `data/gis/route_stop_scenario_layers/` contains the hydrated route, stop, grid, and TOD scenario shapefile layers.
- `data/gis/developable_land_subset_review/` contains land-use and developable-land GIS layers relevant to the Liverpool scenario setup.
- `data/gis/compressed_large_layers/` contains compressed large shapefile bundles retained instead of duplicating loose very large shapefile components.
- `data/access_frequency_matrix/` contains access, iso-access, route-length, frequency matrix, and regression notebooks/tables copied from the existing hydrated 2022-04 Liverpool package.
- `metadata/` and `docs/` contain manifests, checksums, data dictionary, source-file decisions, provenance, and upload notes.

## Release Boundary

This package is public-ready for review because it contains interpretable local data/code/GIS materials that match the paper's described workflow. OpenTripPlanner and QGIS are external runtimes and are documented rather than bundled.

The exact custom OTP batch-query wrapper is not an active hunt item. The paper identifies OTP as the runtime used for isochrone queries but does not establish a separate bespoke wrapper as an expected archive artifact.

The generated scenario zip output names in the live Dropbox GTFS output folder are cloud-only zero-byte entries in the current local copy. They are not included here because the package already carries the generation workflow, inputs, GIS layers, and access/frequency outputs needed for public archive review.

## Upload Mechanics

The current package includes a GTFS source zip of about 131 MB, which is tracked with Git LFS for GitHub upload. The compressed GIS bundles of about 32 MB and 43 MB remain ordinary package files. Local `paper/*.pdf` reference copies are retained on disk for audit convenience but ignored from the public GitHub tree unless redistribution rights are separately cleared.

<!-- package-hardening-status:start -->
## Package Hardening Status

Generated: 2026-05-20 15:32:54 AEST

- Pipeline: `READY-TO-UPLOAD/PUBLIC`
- Sidecars added/updated: `PACKAGE_STATUS.md`, `PACKAGE_MANIFEST.csv`, `LICENSE_STATUS.md`.
- Paper reference copies are for local audit convenience and are not public-upload assets without rights review.
- Final GitHub upload should use the manifest include statuses and the license-status note.
<!-- package-hardening-status:end -->
