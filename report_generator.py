
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# Read data
df = pd.read_csv("sales_data.csv")

# Basic analysis
total_sales = (df['Quantity'] * df['Price']).sum()
total_quantity = df['Quantity'].sum()
average_price = df['Price'].mean()

product_group = df.groupby('Product').agg({
    'Quantity': 'sum',
    'Price': 'mean'
}).reset_index()

# Create PDF
pdf_file = "sales_report.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# Title
story.append(Paragraph("📊 Sales Report", styles['Title']))
story.append(Spacer(1, 12))

# Summary
summary_text = f"""
<b>Total Sales:</b> ₹{total_sales:.2f}<br/>
<b>Total Quantity Sold:</b> {total_quantity}<br/>
<b>Average Price:</b> ₹{average_price:.2f}
"""
story.append(Paragraph(summary_text, styles['Normal']))
story.append(Spacer(1, 12))

# Table for product-wise stats
story.append(Paragraph("Product-wise Summary:", styles['Heading2']))

# Prepare table data
table_data = [['Product', 'Total Quantity', 'Average Price']]
for _, row in product_group.iterrows():
    table_data.append([
        row['Product'],
        int(row['Quantity']),
        f"₹{row['Price']:.2f}"
    ])

# Create and style table
table = Table(table_data, colWidths=[150, 150, 150])
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
]))
story.append(table)

# Build PDF
doc.build(story)
print(f"✅ Report generated: {pdf_file}")

import os
os.startfile("sales_report.pdf")
