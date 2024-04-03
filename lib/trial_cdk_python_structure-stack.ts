import { PythonLayerVersion } from "@aws-cdk/aws-lambda-python-alpha";
import * as cdk from "aws-cdk-lib";
import {
  Architecture,
  Code,
  Function,
  LayerVersion,
  Runtime,
} from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import path from "node:path";

export class TrialCdkPythonStructureStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const layerPowerTools = LayerVersion.fromLayerVersionArn(
      this,
      "LayerPowerTools",
      "arn:aws:lambda:ap-northeast-1:017000801446:layer:AWSLambdaPowertoolsPythonV2-Arm64:68",
    );

    const layerCommon = new PythonLayerVersion(this, "LayerCommon", {
      entry: "src/layers/common",
      layerVersionName: "TrialPythonStructureCommonLayer",
      compatibleRuntimes: [Runtime.PYTHON_3_12],
      compatibleArchitectures: [Architecture.ARM_64],
    });

    new Function(this, "FunctionSample", {
      runtime: Runtime.PYTHON_3_12,
      handler: "sample.handler",
      code: Code.fromAsset(path.join(__dirname, "../src/handlers/sample")),
      architecture: Architecture.ARM_64,
      environment: {
        SYSTEM_NAME: "system-name",
      },
      layers: [layerCommon, layerPowerTools],
    });
  }
}
