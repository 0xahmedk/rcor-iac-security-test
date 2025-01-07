provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "insecure_instance" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"

  tags = {
    Name = "insecure-instance"
  }
}
