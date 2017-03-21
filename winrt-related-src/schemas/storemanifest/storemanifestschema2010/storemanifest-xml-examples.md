---
title: StoreManifest XML example (Windows 8.1 and earlier)
Description: XML example of a StoreManifest XML file for a package targeting Windows 8.1 or earlier.
ms.assetid: 7d6eaaf8-b0f0-4d8a-b2a6-c9a8f90704c9
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, storemanifest
---

# StoreManifest XML example (Windows 8.1 and earlier)


Here's an example of a StoreManifest XML file for a package targeting Windows 8.1 or earlier.

## Single device experience


The following XML file declares the app as a device app that is tied to a single device experience.

```XML
<?xml version="1.0" encoding="utf-8"?>
<StoreManifest
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:noNamespaceSchemaLocation="StoreManifest.xsd"
  xmlns="http://schemas.microsoft.com/appx/2010/StoreManifest">

    <ProductFeatures>
        
        <DeviceCompanionApplication>
            <ExperienceIds>
                <ExperienceId>aeabdaa8-3bcd-4f03-a7f5-54647fd574c2</ExperienceId>
            </ExperienceIds>
        </DeviceCompanionApplication>
                
    </ProductFeatures>
</StoreManifest>
```

 

 



