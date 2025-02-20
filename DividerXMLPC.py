import os
import xml.etree.ElementTree as ET
import webbrowser

def validate_file_path(file_path):
    """Check if the file path exists and is a file."""
    if not os.path.isfile(file_path):
        print(f"Error: The file {file_path} does not exist or is not a file.")
        return False
    return True

def validate_xml_structure(tree):
    """Check if the XML structure contains the expected elements."""
    root = tree.getroot()
    if root.tag != 'TextureAtlas':
        print("Error: The XML file does not have the expected root element 'TextureAtlas'.")
        return False
    if not any(subtexture.tag == 'SubTexture' for subtexture in root.iter('SubTexture')):
        print("Error: No 'SubTexture' elements found in the XML file.")
        return False
    return True

def main():
    ### USER INPUT FOR FILE PATHS ###
    # INPUT #
    input_file = input("Enter the path to the input XML file: ")
    if not validate_file_path(input_file):
        return

    # OUTPUT #
    output_file = input("Enter the path for the output XML file: ")
    if not os.access(os.path.dirname(output_file), os.W_OK):
        print(f"Error: The directory for {output_file} is not writable.")
        return

    # DIVIDE BY? #
    try:
        number = int(input("Enter the division factor (e.g 2): "))
    except ValueError:
        print("Error: Please enter a valid integer for the division factor.")
        return

    ### CODES ###
    try:
        tree = ET.parse(input_file)
    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        return
    except ET.ParseError:
        print(f"Error: The file {input_file} is not a valid XML file.")
        return

    if not validate_xml_structure(tree):
        return

    for subtexture in tree.iter('SubTexture'):
        x = subtexture.get('x')
        y = subtexture.get('y')
        width = subtexture.get('width')
        height = subtexture.get('height')
        fX = subtexture.get('frameX')
        fY = subtexture.get('frameY')
        fW = subtexture.get('frameWidth')
        fH = subtexture.get('frameHeight')

        if x is not None:
            subtexture.set('x', str(int(x) // number))
        if y is not None:
            subtexture.set('y', str(int(y) // number))
        if width is not None:
            subtexture.set('width', str(int(width) // number))
        if height is not None:
            subtexture.set('height', str(int(height) // number))
        if fX is not None:
            subtexture.set('frameX', str(int(fX) // number))
        if fY is not None:
            subtexture.set('frameY', str(int(fY) // number))
        if fW is not None:
            subtexture.set('frameWidth', str(int(fW) // number))
        if fH is not None:
            subtexture.set('frameHeight', str(int(fH) // number))

    try:
        tree.write(output_file, encoding='utf-8', xml_declaration=True)
        print("File Converted Successfully!")
        print(f"INPUT='{os.path.abspath(input_file)}'")
        print(f"OUTPUT='{os.path.abspath(output_file)}'")
    except Exception as e:
        print(f"Error: Could not write to the output file. {e}")
        return

    ### USER CHOICE FOR REDIRECTION ###
    redirect_choice = input("Do you want to be redirected to ResizePixel? (Y/N): ").strip().lower()
    if redirect_choice == 'Y':
        webbrowser.open('https://www.resizepixel.com/') 
    else:
        print("You chose not to be redirected.")

if __name__ == '__main__':
    print("Divider XML PC")
    main()