package com.adrian.enterprise.controller;

import org.springframework.web.bind.annotation.*;
import io.micrometer.core.annotation.Timed;
import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/data")
public class DataController {

    @GetMapping("/items")
    @Timed(value = "api.odata.items", description = "Time taken to return OData items")
    public Map<String, Object> getODataItems() {
        return Map.of(
            "@odata.context", "$metadata#Items",
            "value", List.of(
                Map.of("id", 101, "name", "Enterprise Asset", "status", "Certified")
            )
        );
    }
}

