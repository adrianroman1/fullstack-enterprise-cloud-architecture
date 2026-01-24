package com.adrian.enterprise.controller;

import io.micrometer.core.instrument.MeterRegistry;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.logging.Logger;

@RestController
@RequestMapping("/api/v1/erp")
public class InventoryController {
    private static final Logger logger = Logger.getLogger(InventoryController.class.getName());
    private final MeterRegistry registry;

    public InventoryController(MeterRegistry registry) {
        this.registry = registry;
    }

    @GetMapping("/inventory-status")
    public String getStatus() {
        registry.counter("erp.inventory.access").increment();
        logger.info("Production ERP Status requested.");
        return "ERP System Operational - Java 21 Engine Active";
    }
}
