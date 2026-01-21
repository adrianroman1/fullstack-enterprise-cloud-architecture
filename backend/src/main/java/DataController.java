package com.adrian.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import io.micrometer.core.annotation.Timed;

@RestController
@RequestMapping("/api/v1/data")
public class DataController {

    /**
     * Demonstrates proficiency in OData protocol standards 
     * and system observability using Micrometer.
     */
    @GetMapping("/items")
    @Timed(value = "get.items.time", description = "Time taken to return items")
    public String getODataItems() {
        return "{ \"@odata.context\": \"$metadata#Items\", \"value\": [{\"id\": 1, \"name\": \"Enterprise Component\"}] }";
    }
}
