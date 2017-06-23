import dicom
import gdcm
import sys


filepath='/home/jensen/nutstore/medical_image_processing/tecent_data/20170209/CT/00757360_20170209_055425_CT/'
file1=filepath+'CT_1.2.392.200036.9116.2.6.1.37.2420784083.1486587299.158774.dcm'
file2='./'+'newfile2.dcm'
r = gdcm.ImageReader()
r.SetFileName(file1)
if not r.Read():
    sys.exit(1)
image = gdcm.Image()
ir = r.GetImage()
image.SetNumberOfDimensions( ir.GetNumberOfDimensions() );
dims = ir.GetDimensions();
print ir.GetDimension(0);
print ir.GetDimension(1);
print "Dims:",dims
image.SetDimension(0, ir.GetDimension(0));
image.SetDimension(1, ir.GetDimension(1));
pixeltype = ir.GetPixelFormat();
image.SetPixelFormat(pixeltype);
pi = ir.GetPhotometricInterpretation();
image.SetPhotometricInterpretation(pi);
pixeldata = gdcm.DataElement(gdcm.Tag(0x7fe0,0x0010))
str1 = ir.GetBuffer()
#print ir.GetBufferLength()
pixeldata.SetByteValue(str1, gdcm.VL(len(str1)))
image.SetDataElement(pixeldata)

w = gdcm.ImageWriter()
w.SetFileName(file2)
w.SetFile(r.GetFile())
w.SetImage(image)
if not w.Write():
    sys.exit(1)
print(1)
plan2=dicom.read_file(file2)
print(plan2.pixel_array)
print(plan2.PatientsName)
print(plan2)