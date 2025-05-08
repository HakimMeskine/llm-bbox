# PCB Manufacturing Guide for ESP32 Button Box

This guide provides instructions for preparing the PCB design files for manufacturing with services like PCBway.

## Recommended PCB Design Software

We recommend using [KiCad](https://www.kicad.org/) (free and open-source) for implementing this PCB design. Other options include:
- Altium Designer
- Eagle
- EasyEDA
- Fusion 360 Electronics

## Design Implementation Steps

1. Create a new project in your PCB design software
2. Set up the schematic based on the `schematic_description.txt` file
3. Assign appropriate footprints to all components as listed in the BOM
4. Generate the netlist from the schematic
5. Create a new PCB layout and import the netlist
6. Place components according to the guidelines in `pcb_layout_description.txt`
7. Route the traces following the routing guidelines
8. Add mounting holes, silkscreen labels, and other features
9. Perform design rule checks (DRC) to ensure manufacturability
10. Generate Gerber files for manufacturing

## Generating Gerber Files

Most PCB manufacturers require Gerber files in the RS-274X format. Here's how to generate them in KiCad:

1. From the PCB Editor, click on "File" > "Plot"
2. Select the following layers:
   - F.Cu (Top copper)
   - B.Cu (Bottom copper)
   - F.Paste (Top paste)
   - B.Paste (Bottom paste)
   - F.SilkS (Top silkscreen)
   - B.SilkS (Bottom silkscreen)
   - F.Mask (Top solder mask)
   - B.Mask (Bottom solder mask)
   - Edge.Cuts (Board outline)
3. Set the output directory to a new folder (e.g., "gerber")
4. Check "Use Protel filename extensions"
5. Click "Plot" to generate the Gerber files
6. Click on "Generate Drill Files" to create the drill files
7. In the drill file dialog, select "Excellon" format and click "Generate Drill File"

## Design Rules for Manufacturing

Ensure your design meets these minimum specifications for reliable manufacturing:

- Minimum trace width: 0.2mm (8 mil)
- Minimum spacing: 0.2mm (8 mil)
- Minimum drill size: 0.3mm (12 mil)
- Minimum annular ring: 0.15mm (6 mil)
- Minimum text size: 0.8mm (32 mil)

## Submitting to PCB Manufacturer

1. Compress all Gerber files and drill files into a ZIP archive
2. Upload the ZIP file to your chosen PCB manufacturer's website
3. Specify the following parameters:
   - Board dimensions: 150mm x 100mm (or as adjusted)
   - Material: FR-4
   - Thickness: 1.6mm
   - Copper weight: 1oz
   - Number of layers: 2
   - Surface finish: HASL or ENIG
   - Solder mask color: Green (or preferred color)
   - Silkscreen color: White (or preferred color)
4. Review the design preview provided by the manufacturer
5. Confirm and place the order

## Additional Recommendations

- Request a DFM (Design for Manufacturing) check from the manufacturer
- Consider ordering a small quantity first to verify the design
- Include a README file with your Gerber submission explaining any special requirements
- If possible, include a PDF or image of the expected PCB layout for reference

## Common Issues to Avoid

- Copper too close to board edges (keep at least 0.5mm clearance)
- Silkscreen overlapping pads
- Missing or incorrect drill files
- Incorrect layer assignment
- Insufficient clearance around mounting holes
