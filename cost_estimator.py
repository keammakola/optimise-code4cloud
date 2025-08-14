# cloud_cost.py
"""Realistic AWS pricing (2024) as dictionaries and functions"""

# Pricing tables
PRICING = {
    'lambda': {
        'per_gb_second': 0.0000166667,
        'per_request': 0.0000002
    },
    'ec2': {
        't3.micro': 0.0104  # $/hour
    },
    'rds': {
        't3.micro': 0.017  # $/hour
    },
    'dynamodb': {
        'per_read': 0.00000025  # $/read
    }
}

def calculate_lambda_cost(memory_gb, duration_sec, requests=1):
    """Calculate AWS Lambda costs"""
    return (memory_gb * duration_sec * PRICING['lambda']['per_gb_second'] +
            requests * PRICING['lambda']['per_request'])

def calculate_ec2_cost(hours, instance_type='t3.micro'):
    """Calculate EC2 costs"""
    return hours * PRICING['ec2'][instance_type]

def calculate_rds_cost(hours, instance_type='t3.micro'):
    """Calculate RDS costs"""
    return hours * PRICING['rds'][instance_type]

def calculate_dynamodb_cost(read_units):
    """Calculate DynamoDB read costs"""
    return read_units * PRICING['dynamodb']['per_read']



print(calculate_lambda_cost(1, 1, 5))