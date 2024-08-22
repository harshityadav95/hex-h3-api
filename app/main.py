from typing import Union

from fastapi import FastAPI, HTTPException

import h3


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/v4/latlng_to_cell/")
async def get_latlng_to_cell(latitude: float, longitude: float, resolution: int):
    """
    Receives longitude, latitude, and a resolution number.

    Args:
        longitude (float): The longitude coordinate.
        latitude (float): The latitude coordinate.
        resolution (int): A resolution number.

    Returns:
        str: The H3 cell ID.

    Raises:
        HTTPException: If invalid input is provided or an error occurs during conversion.
    """
    try:
        # Validate latitude and longitude
        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude or longitude")

        # Validate resolution
        if not (0 <= resolution <= 15):
            raise ValueError("Invalid resolution (must be between 0 and 15)")

        # Convert to H3 cell ID
        cell_id = h3.latlng_to_cell(latitude, longitude, resolution)

        return cell_id

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
@app.get("/v4/cell_to_latlng/")
async def get_cell_to_latlng(cell: str):
    """
    Receives an H3 cell ID and returns its latitude and longitude coordinates.

    Args:
        cell (str): The H3 cell ID.

    Returns:
        dict: A dictionary containing the latitude and longitude.

    Raises:
        HTTPException: If an invalid H3 cell ID is provided or an error occurs during conversion.
    """
    try:
        # Convert H3 cell ID to latitude and longitude
        latlng = h3.cell_to_latlng(cell)

        return {"latitude": latlng[0], "longitude": latlng[1]}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    

@app.get("/v4/cell_to_boundary/")
async def get_cell_to_boundary(cell: str):
    """
    Receives an H3 cell ID and returns its boundary coordinates.

    Args:
        cell (str): The H3 cell ID.
      
    Returns:
        list or dict: A list of coordinate tuples if geo_json is False, or a GeoJSON dictionary if geo_json is True.

    Raises:
        HTTPException: If an invalid H3 cell ID is provided or an error occurs during conversion.
    """
    try:
        # Get the cell boundary
        boundary = h3.cell_to_boundary(cell)

        return boundary

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/v4/get_resolution/")
async def get_h3_resolution(h: str):
    """
    Receives an H3 index and returns its resolution.

    Args:
        h (str): The H3 index.

    Returns:
        int: The resolution of the H3 index.

    Raises:
        HTTPException: If an invalid H3 index is provided.
    """
    try:
        resolution = h3.get_resolution(h)
        return {"resolution": resolution}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/v4/get_base_cell_number/")
async def get_h3_base_cell_number(h: str):
    """
    Receives an H3 index and returns its base cell number.

    Args:
        h (str): The H3 index.

    Returns:
        int: The base cell number of the H3 index.

    Raises:
        HTTPException: If an invalid H3 index is provided.
    """
    try:
        base_cell_number = h3.get_base_cell_number(h)
        return {"base_cell_number": base_cell_number}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    

@app.get("/v4/str_to_int/")
async def get_string_to_h3(h: str):
    """
    Receives an H3 index string and returns its H3 integer representation.

    Args:
        h (str): The H3 index string.

    Returns:
        int: The H3 integer representation.

    Raises:
        HTTPException: If an invalid H3 index string is provided.
    """
    try:
        h3_integer = h3.str_to_int(h)
        return {"h3_integer": h3_integer}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/v4/int_to_str/")
async def get_int_to_str(x: int):
    """
    Receives an H3 integer representation and returns its H3 index string.

    Args:
        x (int): The H3 integer representation.

    Returns:
        str: The H3 index string.

    Raises:
        HTTPException: If an invalid H3 integer representation is provided.
    """
    try:
        h3_string = h3.int_to_str(x)
        return {"h3_string": h3_string}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/v4/is_valid_cell/")
async def get_is_valid_cell(cell: str):
    """
    Receives an H3 index and returns whether it is a valid H3 cell.

    Args:
        cell (str): The H3 index.

    Returns:
        bool: True if the H3 index is a valid cell, False otherwise.
    """
    try:
        is_valid = h3.is_valid_cell(cell)
        return {"is_valid": is_valid}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/v4/is_res_class_iii/")
async def get_is_res_class_iii(h: str):
    """
    Receives an H3 index and returns whether it is a Class III resolution cell.
    “Class II” cells have resolutions: 0,2,4,6,8,10,12,14 “Class III” cells have resolutions: 1,3,5,7,9,11,13,15


    Args:
        h (str): The H3 index.

    Returns:
        bool: True if the H3 index is a Class III resolution cell, False otherwise.

    Raises:
        HTTPException: If an invalid H3 index is provided.
    """
    try:
        is_class_iii = h3.is_res_class_III(h)
        print(is_class_iii)

        return {"is_class_iii": is_class_iii}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    


@app.get("/v4/is_pentagon/")
async def get_is_pentagon(h: str):
    """
    Receives an H3 index and returns whether it represents a pentagon cell.

    Args:
        h (str): The H3 index.

    Returns:
        bool: True if the H3 index represents a pentagon cell, False otherwise.

    Raises:
        HTTPException: If an invalid H3 index is provided.
    """
    try:
        is_pentagon = h3.is_pentagon(h)
        return {"is_pentagon": is_pentagon}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/v4/get_icosahedron_faces/")
async def get_icosahedron_faces(h: str):
    """
    Receives an H3 index and returns the icosahedron faces it intersects.

    Args:
        h (str): The H3 index.

    Returns:
        list: A list of integers representing the icosahedron faces.

    Raises:
        HTTPException: If an invalid H3 index is provided.
    """
    try:
        faces = h3.get_icosahedron_faces(h)
        return {"faces": faces}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")