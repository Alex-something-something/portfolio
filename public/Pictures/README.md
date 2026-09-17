# Portfolio picture and video guide

## Adding or replacing media

1. Put your file in the folder listed below, inside `public/Pictures`, with the exact filename and extension.
2. Refresh the page. Use Ctrl + F5 if a replaced image remains cached.
3. The filename placeholder disappears automatically once its image or video loads.

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
| Assembly.png | index.html, project_aerocover.html | Aerocover CAD Image |
| Profile-Comparison.png | project_aerocover.html | Candidate Profile Comparison |
| Baseline-Comparison.png | project_aerocover.html | Icarus Baseline and Argo Concept |
| CFD.png | project_aerocover.html | CFD Visualization |
| FEA.png | project_aerocover.html | Structural Analysis |
| Mold-Mounting.png | project_aerocover.html | Mold or Mounting Concept |

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
| Rings.jpg | manufacturing.html | Turned Rings Photo |

### Pictures/Nozzle

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Isometric.png | index.html, project_nozzle.html | Nozzle CAD image |
| Hotfire.mp4 | project_nozzle.html | Hotfire Test Slow Motion Video/GIF |
| Drawing.png | project_nozzle.html | SolidWorks Drawing |
| FEA.png | project_nozzle.html | FEA Meshing Image |
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
| Assembly.png | index.html | VEGAS image |

### Pictures/Vacuum

| Exact filename | Used on | Image/video |
| --- | --- | --- |
| Chamber.jpg | index.html, project_recovery.html, project_vacuum.html | Vacuum chamber image |
| Pressure-Data.png | project_vacuum.html | PT Data Graph |

## Pages with no existing picture slots

Culturon, APPT, and COSSMo currently have text-only layouts, so no image files are required for them. ME 360 has a homepage image slot; its detail page remains a course placeholder.

## Accessibility

Each loaded image has a descriptive text alternative. Update `data-alt` if your chosen image shows something different. Add captions or a transcript alongside a video if it includes meaningful speech or sound.
