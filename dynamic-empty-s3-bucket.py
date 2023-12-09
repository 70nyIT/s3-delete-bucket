import boto3


def list_buckets(session):
    """List all S3 buckets in the session"""
    s3 = session.client('s3')
    response = s3.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]
    return buckets


def empty_and_delete_bucket(bucket_name, s3_resource):
    """Empty and delete the specified S3 bucket"""
    bucket = s3_resource.Bucket(bucket_name)

    # Empty the bucket
    bucket.objects.all().delete()

    # Delete the bucket
    bucket.delete()
    print(f"Bucket '{bucket_name}' emptied and deleted successfully.")


def main():
    profile_name = str(input("AWS Profile name to use: "))

    # Initialize a session using a profile
    session = boto3.Session(profile_name=profile_name)
    s3_resource = session.resource('s3')

    while True:
        # List all buckets
        buckets = list_buckets(session)
        if not buckets:
            print("No buckets to delete.")
            break

        print("S3 Buckets:")
        for idx, bucket in enumerate(buckets, 1):
            print(f"{idx}. {bucket}")

        try:
            choice = int(input("Enter the number of the bucket to delete (0 to exit): "))
            if choice == 0:
                break
            elif 1 <= choice <= len(buckets):
                bucket_name = buckets[choice - 1]
                empty_and_delete_bucket(bucket_name, s3_resource)
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
