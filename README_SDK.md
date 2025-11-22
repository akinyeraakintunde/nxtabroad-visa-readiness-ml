# NxtAbroad AI – Python SDK Client

This document explains how to use the Python client (`api_client.py`) to interact with the NxtAbroad AI Visa Readiness & Eligibility Intelligence Engine through its FastAPI endpoint.

The SDK provides a simple, reusable interface for integrating the scoring engine into internal tools, dashboards, automation scripts, or external applications.

-------------------------------------------------------------

## 1. Overview

The Python client enables:

- Sending one or more applicant profiles to the `/predict` endpoint  
- Receiving structured scoring results  
- Loading request data from JSON files  
- Handling errors gracefully  
- Easily integrating the engine with other systems  

The client acts as a lightweight SDK for the NxtAbroad AI API.

-------------------------------------------------------------

## 2. Installation

Ensure the project dependencies are installed:
