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