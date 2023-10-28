//
// PhoneVerification.h
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#ifndef DatabaseSystem_PhoneVerification_INCLUDED
#define DatabaseSystem_PhoneVerification_INCLUDED


#include "Poco/ActiveRecord/ActiveRecord.h"


namespace DatabaseSystem {


class PhoneVerification: public Poco::ActiveRecord::ActiveRecord<std::string>
{
public:
	using Ptr = Poco::AutoPtr<PhoneVerification>;

	explicit PhoneVerification(ID id);
	PhoneVerification() = default;
	PhoneVerification(const PhoneVerification& other);
	~PhoneVerification() = default;

	const std::string& phoneProof() const;
	PhoneVerification& phoneProof(const std::string& value);

	const Poco::DateTime& expirationAt() const;
	PhoneVerification& expirationAt(const Poco::DateTime& value);

	bool used() const;
	PhoneVerification& used(bool value);

	static Ptr find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id);

	void insert();
	void update();
	void remove();

	static const std::vector<std::string>& columns();
	static const std::string& table();

private:
	std::string _phoneProof;
	Poco::DateTime _expirationAt;
	bool _used = false;

	friend class Poco::Data::TypeHandler<PhoneVerification>;
};


inline const std::string& PhoneVerification::phoneProof() const
{
	return _phoneProof;
}


inline PhoneVerification& PhoneVerification::phoneProof(const std::string& value)
{
	_phoneProof = value;
	return *this;
}


inline const Poco::DateTime& PhoneVerification::expirationAt() const
{
	return _expirationAt;
}


inline PhoneVerification& PhoneVerification::expirationAt(const Poco::DateTime& value)
{
	_expirationAt = value;
	return *this;
}


inline bool PhoneVerification::used() const
{
	return _used;
}


inline PhoneVerification& PhoneVerification::used(bool value)
{
	_used = value;
	return *this;
}


} // namespace DatabaseSystem


namespace Poco {
namespace Data {


template <>
class TypeHandler<DatabaseSystem::PhoneVerification>
{
public:
	static std::size_t size()
	{
		return 3;
	}

	static void bind(std::size_t pos, const DatabaseSystem::PhoneVerification& ar, AbstractBinder::Ptr pBinder, AbstractBinder::Direction dir)
	{
		TypeHandler<std::string>::bind(pos++, ar._phoneProof, pBinder, dir);
		TypeHandler<Poco::DateTime>::bind(pos++, ar._expirationAt, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._used, pBinder, dir);
}

	static void extract(std::size_t pos, DatabaseSystem::PhoneVerification& ar, const DatabaseSystem::PhoneVerification& deflt, AbstractExtractor::Ptr pExtr)
	{
		TypeHandler<std::string>::extract(pos++, ar._phoneProof, deflt._phoneProof, pExtr);
		TypeHandler<Poco::DateTime>::extract(pos++, ar._expirationAt, deflt._expirationAt, pExtr);
		TypeHandler<bool>::extract(pos++, ar._used, deflt._used, pExtr);
}

	static void prepare(std::size_t pos, const DatabaseSystem::PhoneVerification& ar, AbstractPreparator::Ptr pPrep)
	{
		TypeHandler<std::string>::prepare(pos++, ar._phoneProof, pPrep);
		TypeHandler<Poco::DateTime>::prepare(pos++, ar._expirationAt, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._used, pPrep);
	}
};


} } // namespace Poco::Data


#endif // DatabaseSystem_PhoneVerification_INCLUDED
