use std::path::PathBuf;

use framels::{basic_listing, paths::Paths};
use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn py_basic_listing(list_paths: Vec<PathBuf>) -> PyResult<Vec<PathBuf>> {
    let val: Vec<PathBuf> = basic_listing(Paths::new(list_paths)).get_paths().to_vec();
    Ok(val)
}

#[pymodule]
fn py_framels(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(py_basic_listing, m)?)?;
    Ok(())
}
