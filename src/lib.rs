use std::path::PathBuf;

use framels::{basic_listing, parse_dir, paths::Paths, recursive_dir};
use pyo3::prelude::*;

/// Pack the vector of pathbuf
#[pyfunction]
fn py_basic_listing(list_paths: Vec<PathBuf>, multithreaded: bool) -> PyResult<Vec<PathBuf>> {
    let val: Vec<PathBuf> = basic_listing(Paths::from(list_paths), multithreaded)
        .get_paths()
        .to_vec();
    Ok(val)
}

/// Parse a directory
#[pyfunction]
fn py_parse_dir(path: String, multithreaded: bool) -> PyResult<Vec<PathBuf>> {
    let val: Vec<PathBuf> = basic_listing(parse_dir(&path), multithreaded)
        .get_paths()
        .to_vec();
    Ok(val)
}

/// Walk a directory and his subfolder
#[pyfunction]
fn py_recursive_dir(path: String, multithreaded: bool) -> PyResult<Vec<PathBuf>> {
    let val: Vec<PathBuf> = basic_listing(recursive_dir(&path), multithreaded)
        .get_paths()
        .to_vec();
    Ok(val)
}

#[pymodule]
fn py_framels(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(py_basic_listing, m)?)?;
    m.add_function(wrap_pyfunction!(py_parse_dir, m)?)?;
    m.add_function(wrap_pyfunction!(py_recursive_dir, m)?)?;
    Ok(())
}
