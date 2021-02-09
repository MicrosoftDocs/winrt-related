---
description: Identifies an Internet Information Service (IIS) module to install, update, or uninstall out-of-band on Nano Server.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:IisModule
ms.assetid: 57d7aaf7-95b7-409d-8cad-cba17ca0a903


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:IisModule


Identifies an Internet Information Service (IIS) module to install, update, or uninstall out-of-band on Nano Server.

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
<dd><b>&lt;serverpreview:IisModule&gt;</b></dd>
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
<serverpreview:IisModule Name               = A string between 1 and 32767 
                                              characters in length with a 
                                              non-whitespace character at its 
                                              beginning and end.  
                         ModuleDll          = A string between 1 and 256 
                                              characters in length that  must 
                                              end with ".dll" and cannot 
                                              contain these characters: <, >, 
                                              :, ", |, ?, or *.
                         SchemaFileName?    = A string between 1 and 256 
                                              characters in length that  must 
                                              end with ".xml" and cannot 
                                              contain these characters: <, >, 
                                              :, ", |, ?, or *. >
  <!-- Child elements -->
  ( serverpreview:SectionGroupDefinition
  | serverpreview:SectionDefintion
  | serverpreview:SectionData
  ){0,100}

</serverpreview:IisModule>
```

**Key**

          {} specific range of occurrences

## Attributes and Elements


**Attributes**

| Attribute          | Description                                                                                                                                               | Data type                                                                                                                                     | Required | Default value |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|
| **ModuleDll**      | The name of the DLL file for the module.                                                                                                                  | A string between 1 and 256 characters in length that must end with ".dll" and cannot contain these characters: &lt;, &gt;, :, ", |, ?, or \*. | Yes      |               |
| **Name**           | The name of the module to install, modify, or uninstall. Modules are installed at %WINDIR%\\System32\\Inetsrv.                                            | A string between 1 and 32767 characters in length with a non-whitespace character at its beginning and end.                                   | Yes      |               |
| **SchemaFileName** | The name of the schema file for the module to install, modify, or uninstall. The schema file is installed at %WINDIR%\\System32\\Inetsrv\\Config\\Schema. | A string between 1 and 256 characters in length that must end with ".xml" and cannot contain these characters: &lt;, &gt;, :, ", |, ?, or \*. | No       |               |

 

**Child Elements**

| Child Element                                                                                       | Description                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:SectionGroupDefinition**](element-serverpreview-sectiongroupdefinition-manual.md) | Identifies an Internet Information Service (IIS) SectionGroupDefinition as it pertains to a same-named XML element in an applicationHost.config file. |
| [**serverpreview:SectionDefinition**](element-serverpreview-sectiondefinition-manual.md)           | Identifies an Internet Information Service (IIS) SectionDefinition as it pertains to a same-named XML element in an applicationHost.config file.      |
| [**serverPreview:SectionData**](element-serverpreview-sectiondata-manual.md)                       | Identifies section data that will be embedded into applicationHost.config file of an IIS installation.                                                |

 

**Parent Elements**

| Parent Element                                                              | Description                                                         |
|-----------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**serverpreview:IisModules**](element-serverpreview-iismodules-manual.md) | Declares an app extensibility point of type **windows.iisModules**. |

 

## Remarks


The IIS module extension is only available only on the Windows Server platform. This extension is ignored on other platforms.

The values of the **Name**, **ModuleDll**, and **SchemaFileName** attributes must all be unique.

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
                                    Name="RewriteModule"  
                                    ModuleDll="rewrite.dll"  
                                    SchemaFileName="rewrite_schema.xml">  
                            <serverpreview:SectionGroupDefinition 
                                    Name="rewrite">  
                                <serverpreview:SectionDefinition 
                                    Name="rules"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="globalRules"  
                                    OverrideModeDefault="deny"                    
                                    AllowDefinition="appHostOnly"/>  
                                <serverpreview:SectionDefinition 
                                    Name="outboundRules"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="providers"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="rewriteMaps"  
                                    OverrideModeDefault="allow"/>  
                                <serverpreview:SectionDefinition 
                                    Name="allowedServerVariables"                          
                                    OverrideModeDefault="deny"/>  
                            </serverpreview:SectionGroupDefinition>  
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
| **Namespace** | `http://schemas.microsoft.com/appx/manifest/serverpreview/windows10` |

 

 

 



