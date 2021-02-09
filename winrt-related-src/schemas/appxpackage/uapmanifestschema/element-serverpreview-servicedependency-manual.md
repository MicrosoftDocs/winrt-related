---
description: Specifies an additional service on which the service that corresponds to the grandparent serverpreview:NTService element depends.
Search.Product: eADQiWindows 10XVcnh
title: serverpreview:ServiceDependency
ms.assetid: e0874f7b-4e67-4da6-9f43-2e176f595675


keywords: windows 10, uwp, schema, package manifest


ms.topic: reference
ms.date: 04/05/2017
---

# serverpreview:ServiceDependency


Specifies an additional service on which the service that corresponds to the grandparent [serverpreview:NTService](element-serverpreview-ntservice-manual.md) element depends.

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
<dt><a href="element-serverpreview-ntservices-manual.md">&lt;serverpreview:NTServices&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-ntservice-manual.md">&lt;serverpreview:NTService&gt;</a></dt>
<dd>
<dl>
<dt><a href="element-serverpreview-servicedependencies-manual.md">&lt;serverpreview:ServiceDependencies&gt;</a></dt>
<dd><b>&lt;serverpreview:ServiceDependency&gt;</b></dd>
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
<serverpreview:ServiceDependency Name = A string between 1 and 256 characters in
                                        length with a non-whitespace character 
                                        at its beginning and end. >
</serverpreview:ServiceDependency>
```

## Attributes and Elements


**Attributes**

| Attribute | Description                                                                | Data type                                                                                                 | Required | Default value |
|-----------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------|---------------|
| **Name**  | Specifies the name of the additional service on which the service depends. | A string between 1 and 256 characters in length with a non-whitespace character at its beginning and end. | Yes      |               |

 

**Child Elements**

None.

**Parent Elements**

| Parent Element                                                                                | Description                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**serverpreview:ServiceDependencies**](element-serverpreview-servicedependencies-manual.md) | Specifies the set of additional services on which the service that corresponds to the parent [serverpreview:NTService](element-serverpreview-ntservice-manual.md) element depends. |

 

## Remarks


A service dependency must be one of the other services in the package.

## Examples


```XML
<Package ...
         xmlns:serverpreview=http://schemas.microsoft.com/appx/manifest/serverpreview/windows10"  
         IgnorableNamespaces="... serverpreview">
    <Applications>
       <Application Id="TestService">
            <uap:VisualElements AppListEntry="none" 
                                DisplayName="TestService" 
                                Square150x150Logo="logo.png" 
                                Square44x44Logo="logo.png" 
                                Description="TestService" 
                                BackgroundColor="#777777"/>
            <Extensions>
                <serverpreview:Extension Category="windows.ntServices">  
                    <serverpreview:NTServices>  
                        <serverpreview:NTService  
                                Name="depServiceName"  
                                Executable="depServiceExec.exe"                  
                                StartupType="auto"  
                                StartAccount="networkService"  
                                DisplayName="depServiceName" >       
                        </serverpreview:NTService>             
                        <serverpreview:NTService          
                                Name="serviceName"                     
                                Executable="serviceExec.exe"
                                StartupType="auto"  
                                DisplayName="service Display Name"  
                                StartErrorAction="ignoreError" 
                                StartAccount="localService"    
                                Description="service1 description"   
                                StartParameters="arg1 arg2"
                                FailureRecoveryAction="restartService">
                            <serverpreview:ServiceDependencies>
                                <serverpreview:ServiceDependency 
                                        Name ="depServiceName"/>  
                            </serverpreview:ServiceDependencies>   
                        </serverpreview:NTService> 
                    </serverpreview:NTServices>  
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

 

 

 



