#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test suite for the domain definitions in LASIF.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2014
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import absolute_import

from lasif import domain
from .testing_helpers import images_are_identical, reset_matplotlib


def setup_function(function):
    """
    Reset matplotlib.
    """
    reset_matplotlib()


def test_global_domain_point_in_domain():
    """
    Trivial test...
    """
    d = domain.GlobalDomain()
    assert d.point_in_domain(0, 0)
    assert d.point_in_domain(-90, +90)
    assert d.point_in_domain(0, 180)


def test_plotting_global_domain(tmpdir):
    """
    Tests the plotting of a global domain.
    """
    domain.GlobalDomain().plot(plot_simulation_domain=True)
    images_are_identical("domain_global", str(tmpdir))


def test_plotting_domain_close_to_north_pole(tmpdir):
    """
    Tests the plotting of a domain including the North pole.
    """
    domain.RectangularSphericalSection(
        min_latitude=-30,
        max_latitude=40,
        min_longitude=-30,
        max_longitude=60,
        min_depth_in_km=0,
        max_depth_in_km=1440,
        boundary_width_in_degree=2.0,
        rotation_axis=[0, 1, 0],
        rotation_angle_in_degree=-57.5).plot(plot_simulation_domain=True)
    images_are_identical("domain_with_north_pole", str(tmpdir))


def test_plotting_domain_anatolia(tmpdir):
    """
    Tests plotting of a regional scale domain.
    """
    domain.RectangularSphericalSection(
        min_latitude=34.1,
        max_latitude=42.9,
        min_longitude=23.1,
        max_longitude=42.9,
        min_depth_in_km=0,
        max_depth_in_km=471,
        boundary_width_in_degree=1.46,
        rotation_axis=[0, 0, 1],
        rotation_angle_in_degree=0.0).plot(plot_simulation_domain=True)
    images_are_identical("domain_anatolia", str(tmpdir))


def test_plotting_domain_north_america(tmpdir):
    """
    Tests plotting the North American domain.
    """
    domain.RectangularSphericalSection(
        min_latitude=-25,
        max_latitude=45,
        min_longitude=-120,
        max_longitude=0,
        min_depth_in_km=0,
        max_depth_in_km=1440,
        boundary_width_in_degree=9.0,
        rotation_axis=[0.766044443118978, 0.6427876096865393, 0],
        rotation_angle_in_degree=-30.0).plot(plot_simulation_domain=True)
    images_are_identical("domain_north_america", str(tmpdir))


def test_simple_european_domain(tmpdir):
    """
    Tests the plotting of a simple European domain.
    """
    domain.RectangularSphericalSection(
        min_latitude=-10,
        max_latitude=10,
        min_longitude=-10,
        max_longitude=10,
        min_depth_in_km=0,
        max_depth_in_km=1440,
        boundary_width_in_degree=2.5,
        rotation_axis=[1.0, 1.0, 0.2],
        rotation_angle_in_degree=-65.0).plot(plot_simulation_domain=True)
    images_are_identical("domain_simple_europe", str(tmpdir))


def test_plotting_edge_case__domain(tmpdir):
    """
    Tests the plotting of a heavily deformed domain. Not realistic but
    useful as a test case.
    """
    domain.RectangularSphericalSection(
        min_latitude=-10,
        max_latitude=10,
        min_longitude=-120,
        max_longitude=170,
        min_depth_in_km=0,
        max_depth_in_km=1440,
        boundary_width_in_degree=2.5,
        rotation_axis=[1.0, 1.0, 0.2],
        rotation_angle_in_degree=-75.0).plot(plot_simulation_domain=True)
    images_are_identical("domain_edge_case", str(tmpdir))


def test_domain_new_zealand(tmpdir):
    domain.RectangularSphericalSection(
        min_latitude=-70,
        max_latitude=-10,
        min_longitude=140,
        max_longitude=200,
        min_depth_in_km=0,
        max_depth_in_km=1440,
        boundary_width_in_degree=2.5,
        rotation_axis=[1.0, 1.0, 0.2],
        rotation_angle_in_degree=0.0).plot(plot_simulation_domain=True)
    images_are_identical("domain_new_zealand", str(tmpdir))
