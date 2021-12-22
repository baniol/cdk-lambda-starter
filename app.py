#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_starter.cdk_starter_stack import CdkStarterStack


app = cdk.App()
CdkStarterStack(app, "cdk-starter")

app.synth()
