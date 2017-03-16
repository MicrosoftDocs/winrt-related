---
Description: Represents an attiribute that should be added to or modified in the applicationHost.config file.
MS-HAID: UapManifestSchema.element\_serverpreview\_attribute\_manual
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/apps
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:Attribute
ms.assetid: 8d3d3c80-6411-4912-9bf9-eaa8f9670661
author: laurenhughes
ms.author: lahugh
keywords: windows 10, uwp, schema, package manifest
---

# serverpreview:Attribute


Represents an attiribute that should be added to or modified in the applicationHost.config file.

## Element hierarchy

<dl>
<dt><a href="element-package.md">&lt;Package&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-applications.md">&lt;Applications&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-application.md">&lt;Application&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-1-extensions.md">&lt;Extensions&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-extension-manual.md">&lt;serverpreview:Extension&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-iismodules-manual.md">&lt;serverpreview:IisModules&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-iismodule-manual.md">&lt;serverpreview:IisModule&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-sectiondata-manual.md">&lt;serverpreview:SectionData&gt;</a></dt>
<dd><b>&lt;serverpreview:Attribute&gt;</b></dd>
</dl>									
</dd>
</dl>									
</dd>
</dl>									
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>
</dd>
</dl>

## Syntax


```
<serverpreview:Attribute Name = A string between 1 and 32767 characters in 
                                 length with a non-whitespace character at its 
                                 beginning and end.
                         Value = A string between 1 and 32767 characters in 
                                 length with a non-whitespace character at its 
                                 beginning and end. >
</serverpreview:Attribute>
```

## Attributes and Elements


**Attributes**

| Attribute | Description                 | Data type                                                                                                   | Required | Default value |
|-----------|-----------------------------|-------------------------------------------------------------------------------------------------------------|----------|---------------|
| Name      | The name of the attribute   | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes      |               |
| Value     | The value of the attribute. | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end. | Yes      |               |

 

**Child Elements**

None

.

**Parent Elements**

| Parent Element                                                                | Description                                                                                            |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [**serverpreview:SectionData**](element-serverpreview-sectiondata-manual.md) | Identifies section data that will be embedded into applicationHost.config file of an IIS installation. |

 

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
        <Application>
            <Extensions>
                <serverpreview:Extension Category="windows.iisModules">  
                    <serverpreview:IisModules>  
                        <serverpreview:IisModule 
                                    Name="HypotheticalModule"  
                                    ModuleDll="hypothetical.dll"  
                                    SchemaFileName="hypothetical_schema.xml">  
                            <serverpreview:SectionData 
                                    SectionPath="hypothetical">  
                                <serverpreview:CollectionElement 
                                    Name="ruleNumber1"  
                                    Rule="someRule"/>  
                                <serverpreview:Attribute 
                                    Name="Attribute for hypothetical"  
                                    Value="value"/>  
                                <serverpreview:Attribute 
                                    Name="hostAffinityProviderListAttribute"                    
                                    Value="attributeValue"/>  
                            </serverpreview:SectionData>  
                        </serverpreview:IisModule>  
                    </serverpreview:IisModules> 
                </serverpreview:Extension>  
            </Extensions>
        </Application>
    </Applications>
</Package>
```

## Requirements


|               |                                                                    |
|---------------|--------------------------------------------------------------------|
| **Namespace** | http://schemas.microsoft.com/appx/manifest/serverpreview/windows10 |

 

 

 



