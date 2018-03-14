# RPM package for Ansible dynamic inventory EC2

This package provides build files for a RPM package including the dynamic
inventory script released with Ansible 2.4 upstream branch. 

## Prerequisites

* RPM build environment ex. https://github.com/mhutter/docker-rpmbuild/

The script is working with Ansible 2.4 (or newer).

## Getting started

The package contain the script ec2.py and ec2.ini from the upstream Ansible
repository: https://github.com/ansible/ansible/tree/stable-2.4/contrib/inventory

If you searching for a manual, you may find the ressources here:

* http://docs.ansible.com/ansible/latest/intro_dynamic_inventory.html#example-aws-ec2-external-inventory-script
* https://aws.amazon.com/blogs/apn/getting-started-with-ansible-and-dynamic-amazon-ec2-inventory-management/

## Contributions

Each contribution is very welcome--be it an issue or a pull request. We're
happy to accept pull requests so long as they meet the existing code quality
and design.

1. Fork repository (https://github.com/appuio/ansible-dynamic-inventory-ec2/fork)
2. Create feature branch (`git checkout -b my-new-feature`)
3. Commit changes (`git commit -av`)
4. Push to branch (`git push origin my-new-feature`)
5. Create a pull request

## License

GPL 3.0

## Author Information

APPUiO Team <info@appuio.ch>
