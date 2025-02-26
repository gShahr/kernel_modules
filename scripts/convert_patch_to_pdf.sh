#!/bin/bash
# Usage: ./patch2pdf.sh input.patch [output.pdf]
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <patch_file> [output_pdf]"
    exit 1
fi

PATCH_FILE="$1"
OUTPUT_PDF="${2:-${PATCH_FILE%.*}.pdf}"

# Check that the patch file exists
if [ ! -f "$PATCH_FILE" ]; then
    echo "Error: File $PATCH_FILE not found."
    exit 1
fi

# Convert patch file to PDF
enscript "$PATCH_FILE" -p - | ps2pdf - "$OUTPUT_PDF"

if [ "$?" -eq 0 ]; then
    echo "PDF generated successfully: $OUTPUT_PDF"
else
    echo "Failed to generate PDF."
fi