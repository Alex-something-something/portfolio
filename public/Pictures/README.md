# Portfolio picture and video guide

## Adding or replacing media

1. Put your file in the folder listed below, inside `public/Pictures`, with the exact filename and extension.
2. Refresh the page. Use Ctrl + F5 if a replaced image remains cached.
3. Missing media stays hidden. The image or video appears automatically once the matching file loads.

Use real JPG, PNG and MP4 files matching the extensions. Renaming an extension does not convert the file. Match capitalization for future web hosting. Photos on cards are cropped to fit; PNG diagrams and detail-page images show the whole image. Videos use playback controls and do not autoplay.

The headshot already exists. The same file can appear on a homepage card and its project page, so it only needs to be supplied once. The animated Argo blueprint and hero launch are drawn in code; they do not need picture files.

To change a slot later, edit its `data-media` path and `data-alt` description in the corresponding file under `content/`. Captions remain in those content files.

## Required filenames by folder

### Pictures

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Headshot.jpg | index.html | Portrait of Alexander Tong |

### Pictures/AIAA

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Aircraft.jpg | index.html, dbf.html | Wing design image |
| Prototype-1.png | dbf.html | Prototype 1 Wing CAD or Photo |
| Design-Review.png | dbf.html | Trade Study or Design Review Graphic |
| Prototype-2.png | dbf.html | Prototype 2 Wing CAD or Drawing |
| Fiberglass-Layup.jpg | dbf.html | Fiberglass Layup Process Photo |
| Completed-Layup.jpg | dbf.html | Completed Fiberglass Layup Photo |

### Pictures/Aerocover

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Assembly.png | index.html, project_aerocover.html | Aerodynamic downcomer fairing CAD |
| Profile-Comparison.png | project_aerocover.html | Candidate Profile Comparison |
| Baseline-Comparison.png | project_aerocover.html | Icarus Baseline and Argo Concept |
| CFD.png | Reserved until results are approved | CFD visualization |
| FEA.png | Reserved until results are approved | Structural analysis |
| Carbon-Fiber-Thermal-Load-Test.jpg | project_aerocover.html | Curved carbon-fiber test article and heated static-load setup |

### Pictures/CO2

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Assembly.png | index.html, project_co2.html | CO₂ deployment hardware image |
| Machined-Parts.jpg | project_co2.html | Machined CO₂ Deployment Hardware Photo |

### Pictures/ME360

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Project.jpg | index.html | Course Project Photo |

### Pictures/Manufacturing

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Hammer.jpg | index.html, manufacturing.html | Machining image |

### Pictures/Nozzle

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Isometric.png | index.html, project_nozzle.html | Nozzle CAD image |
| Hotfire.mp4 | project_nozzle.html | Hotfire Test Slow Motion Video/GIF |
| Mounting-Cross-Section.png | project_nozzle.html | Nozzle and mounting-adapter cross-section |
| Drawing.png | project_nozzle.html | SolidWorks Drawing |
| Rao-Angle-Reference.png | project_nozzle.html | Parabolic-nozzle angle reference chart |
| Bezier-Geometry.png | project_nozzle.html | CAD Bézier-curve geometry |
| Bezier-Points.png | project_nozzle.html | Published Rao parabolic-contour construction reference |
| FEA.png | project_nozzle.html | FEA Meshing Image |
| FEA-FOS.png | project_nozzle.html | Calculated yield FOS result |
| FEA-Von-Mises.png | project_nozzle.html | von Mises stress result |
| FEA-Fixturing.png | project_nozzle.html | Bolt-fixture boundary conditions |
| Pressure-Chamber.png | Archived; not displayed | Chamber-pressure load region |
| Pressure-Throat.png | Archived; not displayed | Throat-pressure load region |
| Pressure-External.png | Archived; not displayed | External and diverging-section pressure loads |
| Calculations.png | project_nozzle.html | Calculation Spreadsheet |

### Pictures/Plummer

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Lab-Overview.jpg | plummer.html | Dynamic-Test Fixture or Laboratory Photo |
| Shaker-Analysis.png | plummer.html | Shaker-Adapter CAD or FEA |
| Machined-Plate.jpg | plummer.html | Machined Plate Photo |
| Camera-Stand.jpg | plummer.html | Camera-Mount or Lab Buildout Photo |
| Lab-Fixtures.jpg | plummer.html | Laboratory Layout or Fixture Photo |

### Pictures/Recovery

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Assembly.png | index.html, project_recovery.html | Recovery system image |
| Subscale-Test.mp4 | project_recovery.html | Hero Image/GIF of Subscale Testing |
| Lines-Diagram.png | project_recovery.html | Lines Diagram |
| Connections.png | project_recovery.html | Simplified Connection Diagram |
| Hardware-Assembly.jpg | project_recovery.html | Recovery Hardware Assembly Photo |
| Cable-Cutter-Drawing.png | project_recovery.html | Cable-Cutter Engineering Drawing |
| Cable-Cutters.jpg | project_recovery.html | Machined Cable-Cutter Hardware Photo |
| Line-Verification.mp4 | project_recovery.html | Recovery-Line Verification Video |
| Subscale-Launch.jpg | project_recovery.html | Subscale Rocket Retrofit and Launch Photo |
| Packing-Plan.png | project_recovery.html | Detailed Packing Plan / Nosecone Diagram |

### Pictures/Robot

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Vehicle.jpg | index.html, robot.html | Vehicle image |
| Chassis.png | robot.html | Chassis CAD or Assembly Photo |
| Course-Test.jpg | robot.html | Course-Test Photo or Results Plot |
| Wiring.png | robot.html | Sensor Layout or Wiring Diagram |

### Pictures/VEGAS

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Assembly.png | index.html | VEGAS fire-suppression assembly mounted to the test stand |

### Pictures/Vacuum

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Chamber.jpg | index.html, project_recovery.html, project_vacuum.html | Vacuum chamber image |
| Pressure-Data.png | project_vacuum.html | Pressure-transducer output, analyzed by project partner |
| Door-CAD.png | project_vacuum.html | Vacuum-chamber door and tube-adapter CAD |
| Door-FEA.png | project_vacuum.html | Door finite-element model and stress result |

## Pages using code-drawn visuals

Culturon and Plummer include sanitized, code-drawn engineering diagrams that require no image files. APPT and COSSMo currently have text-only layouts. ME 360 has a homepage image slot; its detail page remains a course placeholder.

## Accessibility

Each loaded image has a descriptive text alternative. Update `data-alt` if your chosen image shows something different. Add captions or a transcript alongside a video if it includes meaningful speech or sound.
